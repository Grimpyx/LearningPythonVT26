def histogram(max_bar, labels, counts):
    
    maxCount = max(counts.values())
    lines = []

    for label in labels:
        number = counts.get(label, 0)
        lines.append(label.ljust(10) + "*" * int(number/maxCount * max_bar))
    
    print("\n".join(lines))

counts = {"pig": 19, "cat":57, "wolf":42, "horse":26}
labels = ["horse", "pig", "cat"]
histogram(20, labels, counts)