"""Опыт 1: одна и та же фраза на русском и английском через токенайзер.

Используется tiktoken (кодировки OpenAI). Токенайзеры Claude не публичны,
поэтому это приближение, но принцип разбиения тот же (BPE).
"""
import sys
import tiktoken

sys.stdout.reconfigure(encoding="utf-8")

PHRASES = {
    "en": "Connect the repository to this folder",
    "ru": "Подключи репозиторий к этой папке",
    "ru_translit": "Podklyuchi repozitoriy k etoy papke",
    "kk": "Репозиторийді осы қалтаға қос",
}
ENCODINGS = ["cl100k_base", "o200k_base"]


def show(enc_name: str) -> None:
    enc = tiktoken.get_encoding(enc_name)
    print(f"=== {enc_name} ===")
    for lang, text in PHRASES.items():
        ids = enc.encode(text)
        # декодируем каждый токен отдельно; для неполных UTF-8 байтов — replace
        pieces = [enc.decode_single_token_bytes(i).decode("utf-8", errors="replace") for i in ids]
        print(f"[{lang}] {text!r}")
        print(f"  символов: {len(text)}, байт UTF-8: {len(text.encode('utf-8'))}, токенов: {len(ids)}")
        print(f"  символов на токен: {len(text) / len(ids):.2f}")
        print(f"  токены: {pieces}")
        print(f"  id:     {ids}")
    en = len(enc.encode(PHRASES["en"]))
    for lang in PHRASES:
        if lang != "en":
            n = len(enc.encode(PHRASES[lang]))
            print(f"Отношение {lang}/en по токенам: {n / en:.2f}")
    print()


if __name__ == "__main__":
    for name in ENCODINGS:
        show(name)
