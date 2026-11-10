"""Опыт 3: корпус тестов через токенайзеры Claude (count_tokens) и OpenAI (tiktoken).

Токены Claude считаются через API: POST /v1/messages/count_tokens
(бесплатный эндпоинт, но нужен ANTHROPIC_API_KEY). tiktoken даёт только базовую
линию для сравнения, для Claude он неточен.

Запуск:
    python experiment3_claude_tokenizer.py

Результат: results/experiment3_results.json и results/experiment3_results.md
"""
import json
import os
import sys
import time
from pathlib import Path

import tiktoken

from corpus import TESTS

sys.stdout.reconfigure(encoding="utf-8")

CLAUDE_MODELS = [
    "claude-fable-5-2",
    "claude-opus-5-5",
    "claude-sonnet-5-5",
    "claude-haiku-5-5",
    "claude-opus-4-6",   # старый токенайзер, для сравнения
    "claude-haiku-4-5",  # старый токенайзер, для сравнения
]
TIKTOKEN_ENCODINGS = ["cl100k_base", "o200k_base"]
OUT_DIR = Path(__file__).parent / "results"


def tiktoken_counts() -> dict:
    out = {}
    for name in TIKTOKEN_ENCODINGS:
        enc = tiktoken.get_encoding(name)
        out[f"tiktoken:{name}"] = {t["id"]: len(enc.encode(t["text"])) for t in TESTS}
    return out


def count_claude(client, model: str, text: str) -> int:
    import anthropic

    for attempt in range(6):
        try:
            resp = client.messages.count_tokens(
                model=model,
                messages=[{"role": "user", "content": text}],
            )
            return resp.input_tokens
        except anthropic.RateLimitError:
            time.sleep(2 ** attempt)
    raise RuntimeError("rate limited too long")


def claude_counts() -> tuple[dict, dict]:
    """Возвращает (счётчики по моделям, ошибки по моделям)."""
    import anthropic

    client = anthropic.Anthropic()
    counts, errors = {}, {}
    for model in CLAUDE_MODELS:
        try:
            # накладные расходы на обёртку сообщения: считаем почти пустой текст
            overhead = count_claude(client, model, ".")
            per_test = {}
            for t in TESTS:
                raw = count_claude(client, model, t["text"])
                per_test[t["id"]] = raw
            counts[f"claude:{model}"] = per_test
            counts[f"claude:{model}"]["__overhead__"] = overhead
            print(f"{model}: ok (накладные расходы по '.' = {overhead})")
        except (anthropic.NotFoundError, anthropic.BadRequestError,
                anthropic.PermissionDeniedError) as e:
            errors[model] = f"{type(e).__name__}: {e}"
            print(f"{model}: пропущено, {errors[model]}")
    return counts, errors


def build_markdown(counts: dict, errors: dict) -> str:
    cols = list(counts)
    lines = ["# Опыт 3. Результаты", ""]
    lines.append("Числа Claude — сырой `input_tokens` из `count_tokens`; в него входят накладные "
                 "расходы на обёртку сообщения (см. строку `overhead`). Для сравнения языков "
                 "они вычтены в таблицах отношений.")
    lines.append("")
    # Таблица по тестам
    header = ["id", "символов", "байт"] + [c.replace("claude:", "").replace("tiktoken:", "tk:") for c in cols]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "---|" * len(header))
    for t in TESTS:
        row = [t["id"], str(len(t["text"])), str(len(t["text"].encode("utf-8")))]
        row += [str(counts[c].get(t["id"], "—")) for c in cols]
        lines.append("| " + " | ".join(row) + " |")
    ov = ["overhead", "", ""] + [str(counts[c].get("__overhead__", "")) for c in cols]
    lines.append("| " + " | ".join(ov) + " |")
    lines.append("")

    # Отношения к английскому внутри групп (с вычетом overhead)
    lines.append("## Отношение к английскому (токены языка / токены en), накладные расходы вычтены")
    lines.append("")
    groups = {}
    for t in TESTS:
        if t["group"] != "single":
            groups.setdefault(t["group"], {})[t["lang"]] = t["id"]
    header = ["группа", "язык"] + [c.replace("claude:", "").replace("tiktoken:", "tk:") for c in cols]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "---|" * len(header))
    for g, langs in groups.items():
        en_id = langs["en"]
        for lang, tid in langs.items():
            if lang == "en":
                continue
            row = [g, lang]
            for c in cols:
                ov = counts[c].get("__overhead__", 1) - 1 if c.startswith("claude:") else 0
                en = counts[c][en_id] - ov
                x = counts[c][tid] - ov
                row.append(f"{x / en:.2f}")
            lines.append("| " + " | ".join(row) + " |")
    lines.append("")
    if errors:
        lines.append("## Модели, которые не удалось проверить")
        lines.append("")
        for m, e in errors.items():
            lines.append(f"- `{m}`: {e}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    counts = tiktoken_counts()
    errors = {}
    if os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"):
        c, errors = claude_counts()
        counts = {**c, **counts}
    else:
        print("ANTHROPIC_API_KEY не задан: считаю только tiktoken (базовая линия).")
    (OUT_DIR / "experiment3_results.json").write_text(
        json.dumps({"tests": TESTS, "counts": counts, "errors": errors},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (OUT_DIR / "experiment3_results.md").write_text(build_markdown(counts, errors), encoding="utf-8")
    print(f"Сохранено в {OUT_DIR}")


if __name__ == "__main__":
    main()
