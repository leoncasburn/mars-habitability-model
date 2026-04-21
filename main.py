import matplotlib.pyplot as plt

# Weighting of scores
weights = {
    "radiation": 25,
    "desiccation": 25,
    "cold": 20,
    "anaerobic": 20,
    "spore_formation": 10
}

organisms = {
    "Deinococcus radiodurans": {
        "radiation": 1.0,
        "desiccation": 1.0,
        "cold": 0.5,
        "anaerobic": 0.0,
        "spore_formation": 0.0
    },
    "Bacillus subtilis": {
        "radiation": 0.5,
        "desiccation": 1.0,
        "cold": 0.5,
        "anaerobic": 0.5,
        "spore_formation": 1.0
    },
    "Halobacterium salinarum": {
        "radiation": 0.5,
        "desiccation": 0.5,
        "cold": 0.0,
        "anaerobic": 0.5,
        "spore_formation": 0.0
    },
    "Escherichia coli": {
        "radiation": 0.0,
        "desiccation": 0.0,
        "cold": 0.0,
        "anaerobic": 1.0,
        "spore_formation": 0.0
    },
    "Pseudomonas aeruginosa": {
        "radiation": 0.0,
        "desiccation": 0.5,
        "cold": 0.0,
        "anaerobic": 0.5,
        "spore_formation": 0.0
    }
}

# Function to score organisms
def score(organisms, weights):
    scores = {}

    for name, traits in organisms.items():
        total_score = 0
        trait_scores = {}

        for trait, value in traits.items():
            weight = weights[trait]
            contribution = value * weight

            trait_scores[trait] = contribution
            total_score += contribution

        trait_scores["total"] = total_score
        scores[name] = trait_scores

    return scores


results = score(organisms, weights)

traits = ["radiation", "desiccation", "cold", "anaerobic", "spore_formation"]

colors = {
    "radiation": "red",
    "desiccation": "orange",
    "cold": "blue",
    "anaerobic": "green",
    "spore_formation": "purple"
}

# Sort organisms by total score
sorted_results = sorted(
    results.items(),
    key=lambda x: x[1]["total"],
    reverse=True
)

# Get sorted organism names
names = [item[0] for item in sorted_results]

bottom = [0] * len(names)

for trait in traits:
    trait_values = [results[name][trait] for name in names]

    plt.bar(
        names,
        trait_values,
        bottom=bottom,
        label=trait,
        color=colors[trait]
    )

    bottom = [
        bottom[i] + trait_values[i]
        for i in range(len(bottom))
    ]

# Printing Results
print("Mars Habitability Rankings:")
for name in names:
    print(name, ":", results[name]["total"])

for i, total in enumerate(bottom):
    plt.text(i, total + 1, str(round(total, 1)), ha="center")

plt.xlabel("Organism Name")
plt.ylabel("Mars Survival Score")
plt.title("Mars Habitability Scores by Trait Contribution")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.show()