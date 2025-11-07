def shadow(limit=200):
    def decorator(gen_func):
        def wrapper(*args, **kwargs):
            gen = gen_func(*args, **kwargs)
            total = 0.0
            over = False
            for item in gen:
                print(item)
                parts = item.strip().split()
                if len(parts) != 2:
                    print("  [тінь] некоректно — ігнорую")
                    yield item
                    continue
                kind, amt = parts[0].lower(), parts[1]
                if kind not in ("payment", "transfer", "refund"):
                    print("  [тінь] невідомий тип — ігнорую")
                    yield item
                    continue
                try:
                    a = float(amt)
                except ValueError:
                    print("  [тінь] сума не число — ігнорую")
                    yield item
                    continue
                total += -a if kind == "refund" else a
                if total > limit and not over:
                    print("  Тіньовий ліміт перевищено. Активую схему")
                    over = True
                if total <= limit:
                    over = False
                yield item
            return total
        return wrapper
    return decorator

def txs():
    yield "payment 120"
    yield "refund 50"
    yield "transfer 300"
    yield "bad entry"
    yield "payment notanumber"
    yield "payment 10.5"
    return 999  

@shadow(limit=200)
def decorated_txs():
    yield from txs()

if __name__ == "__main__":
    g = decorated_txs()
    try:
        while True:
            next(g)
    except StopIteration as e:
        print("\nФінальна сума:", e.value)
