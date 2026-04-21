# Mars Habitability Model

## Overview

This project is a simplified computational model that evaluates how well different microorganisms might tolerate life on Mars.

It assigns scores based on key biological traits that are relevant to survival in a Mars-like environment.

These include:

* Radiation resistance
* Desiccation tolerance
* Cold tolerance
* Anaerobic survival
* Spore formation

The goal is not to predict actual life on Mars, but to investigate how known biological characteristics can be used to model environmental compatibility in an astrobiological context.


## Features

* Trait-based scoring system (0–100 scale)
* Weighted contributions for each trait
* Comparison of multiple microorganisms
* Sorted rankings by total habitability score
* Stacked bar chart showing trait contributions
* Clear, interpretable model structure


## Biological Motivation

Mars presents several extreme environmental challenges:

* High radiation exposure (thin atmosphere)
* Extreme dryness (desiccation)
* Low temperatures
* Limited oxygen availability
* Nutrient-poor conditions

This model evaluates organisms based on how well they tolerate these conditions using simplified trait scores.


## Scoring System

Each organism is assigned trait values:

* `1.0` = strong evidence of tolerance
* `0.5` = moderate/partial tolerance
* `0.0` = little to no tolerance

Traits are weighted as follows:

* Radiation = 25
* Desiccation = 25
* Cold = 20
* Anaerobic = 20
* Spore Formation = 10

Final score = sum of (trait value × weight)


## Example Output

Mars Habitability Rankings:

Deinococcus radiodurans : 60.0
Bacillus subtilis : 55.0
Halobacterium salinarum : 32.5
Pseudomonas aeruginosa : 20.0
Escherichia coli : 20.0


## Visualisation

The model generates a stacked bar chart where:

* Each bar represents an organism
* Each coloured segment represents a trait contribution
* The total height represents the final Mars survival score

This makes the model clear and easy to interpret.


## Technologies Used

* Python
* matplotlib (data visualisation)
* Dictionaries and nested data structures
* Basic data modelling and scoring logic


## Limitations

* Trait scores are simplified (0, 0.5, 1)
* Lacks full biological complexity
* No environmental simulation
* Not intended as a predictive scientific model


## Future Improvements

* Add more organisms
* Expand trait set (e.g. metabolism type)
* Allow custom user-defined organisms
* Export results to CSV
* Build a simple GUI


## Author

This project was created to explore how computational models can be used to represent biological concepts.
