## ADR-001: Missing Head-to-Head Data

### Decision
If two teams have never played each other, the Head-to-Head component is excluded from the strength score calculation.

The remaining components are normalized back to a score out of 100.

### Rationale
Missing historical data should not penalize either team. Normalization preserves comparability between teams while avoiding assumptions about head-to-head performance.

### Example
76/90 becomes 84.44/100.

## ADR-002

Tournament importance is based on the importance of a team’s recent competitive matches rather than historical tournament achievements. Match outcomes are weighted by tournament category and normalized into the 15-point Tournament Importance component.

# ADR-003: Team Strength Score Design

**Status:** Accepted

---

## Context

The World Cup Prediction Platform requires a single numerical value representing a team's current strength. This score serves as the foundation of the rule-based prediction engine and will later be used as a feature in the machine learning model.

The score must be:

- Explainable
- Reproducible
- Based on measurable football statistics
- Easy to extend as additional analytics are introduced

---

## Decision

A team's Strength Score is calculated as a weighted combination of independent analytics components.

### Version 1 Components

| Component | Maximum Points |
|-----------|---------------:|
| Recent Form | 35 |
| Overall Win Percentage | 25 |
| Goal Difference | 15 |
| Tournament Importance | 15 |
| Head-to-Head | 10 |
| **Total** | **100** |

The weights reflect the belief that recent performance is more predictive than historical performance while still recognising long-term consistency and quality of opposition.

---

## Component Definitions

### Recent Form (35 Points)

Calculated using the team's **10 most recent matches**.

Measures:

- Wins
- Draws
- Losses
- Points earned
- Goals scored
- Goals conceded
- Goal difference
- Form string

Recent Form is considered the strongest indicator of current team strength.

---

### Overall Win Percentage (25 Points)

Calculated using the team's historical match record.

Measures long-term consistency rather than short-term momentum.

---

### Goal Difference (15 Points)

Calculated using the team's **10 most recent matches**.

Average goal difference per match is used rather than cumulative goal difference to avoid favouring teams with larger historical datasets.

---

### Tournament Importance (15 Points)

Calculated using the team's **10 most recent matches**.

Match results are weighted according to tournament category rather than treating every competition equally.

Tournament categories include:

- FIFA World Cup
- Continental Championships
- Qualification Competitions
- Regional Competitions
- Friendlies

---

### Head-to-Head (10 Points)

Head-to-Head is only calculated when comparing two specific teams.

If no historical meetings exist, the Head-to-Head component is excluded and the remaining components are normalised back to a score out of 100.

No assumptions are made about missing data.

---

## Strength Score Responsibility

`StrengthScoreService` is responsible for combining existing analytics into a single strength score.

It does **not** calculate raw statistics or query the database directly for analytics.

Instead, it composes existing analytics services, including:

- Team Summary
- Recent Form
- Tournament Importance
- Head-to-Head (during prediction)

This avoids duplicate business logic and follows the **Single Responsibility Principle**.

---

## Design Decisions

### Reuse Existing Analytics

The Strength Score reuses existing analytics services instead of recalculating statistics.

**Benefits**

- Single source of truth
- Reduced code duplication
- Easier maintenance
- Easier testing

---

### Private Scoring Methods

Each scoring component is calculated independently using private helper methods.

Example:

- `_recent_form_score()`
- `_win_percentage_score()`
- `_goal_difference_score()`

This keeps the main calculation method concise while making future extensions straightforward.

---

### Head-to-Head Exclusion

Head-to-Head is **not** considered an intrinsic property of a team.

It is a property of a specific matchup.

Therefore, it is excluded from the standalone Strength Score and incorporated only during match prediction.

---

## Future Enhancements

The architecture is intentionally designed to support additional components without changing existing analytics.

Planned additions include:

- Major Tournament Performance
- Home Advantage
- Continental Advantage
- FIFA/Elo Ranking
- Squad Strength
- Player Availability
- Machine Learning feature integration

---

## Consequences

### Positive

- Modular architecture
- Explainable scoring system
- Easy to tune weighting values
- Easy integration with machine learning
- Reuse of existing analytics services
- Minimal code duplication

### Negative

- The initial rule-based model may not capture all interactions between variables.
- Weight values are manually defined and require validation against historical match data before production use.

---

## Version History

### Version 1

| Component | Weight |
|-----------|-------:|
| Recent Form | 35 |
| Overall Win Percentage | 25 |
| Goal Difference | 15 |
| Tournament Importance | 15 |
| Head-to-Head | 10 |
| **Total** | **100** |

Future versions may introduce additional features such as home advantage, squad strength, Elo ratings, and machine learning predictions while maintaining backward compatibility with the existing architecture.

# ADR-004: Rule-Based Prediction Engine

**Status:** Accepted

---

## Context

The project aims to predict football match outcomes using historical data.

Before introducing machine learning, an explainable prediction model was required to:

- Validate the prediction pipeline.
- Establish a performance baseline.
- Provide transparent reasoning for every prediction.
- Produce deterministic and reproducible results.

---

## Decision

The first version of the prediction platform uses a rule-based prediction engine.

The engine combines multiple analytics services to calculate a numerical strength score for each team before determining the predicted winner.

The prediction process consists of:

1. Calculate each team's Strength Score.
2. Compare the two scores.
3. Apply Head-to-Head adjustment when appropriate.
4. Determine prediction confidence.
5. Generate a human-readable explanation.

The prediction engine orchestrates existing services and does not calculate statistics directly.

---

## Rationale

A rule-based system offers several advantages during early development:

- Fully explainable predictions.
- Easy debugging.
- Deterministic outputs.
- Simple validation against historical matches.
- Serves as a benchmark for future machine learning models.

---

## Consequences

### Positive

- Transparent predictions.
- Modular architecture.
- Easy to tune scoring rules.
- Provides a baseline for ML evaluation.

### Negative

- Scoring weights require manual calibration.
- Complex relationships between variables cannot be learned automatically.

# ADR-005: Dynamic Head-to-Head Adjustment

**Status:** Accepted

---

## Context

Early testing revealed situations where a team with strong historical dominance over another was predicted to lose solely due to recent form.

Example:

- Portugal had won 6 of the previous 7 meetings against Croatia.
- Croatia was predicted to win because of stronger recent statistics.

This reduced confidence in the prediction model.

---

## Decision

Head-to-Head statistics are treated as a decision adjustment rather than a core strength metric.

The adjustment is only applied when:

- The teams have played at least five previous matches.
- Their calculated strength scores differ by no more than five points.

When both conditions are satisfied, the team with the superior Head-to-Head record receives a configurable bonus.

---

## Rationale

Historical matchups provide useful context only when teams are otherwise closely matched.

Applying Head-to-Head universally would allow outdated historical results to dominate predictions.

Restricting its use preserves the importance of current team quality while recognising consistent matchup advantages.

---

## Consequences

### Positive

- More realistic close-game predictions.
- Prevents historical results from overpowering recent performance.
- Maintains explainability.

### Negative

- Introduces additional configuration parameters.
- Requires empirical tuning as the model evolves.

# ADR-006: Explainable Predictions

**Status:** Accepted

---

## Context

Prediction systems often return only a predicted winner without explaining the reasoning.

This makes debugging difficult and reduces user confidence.

---

## Decision

Predictions include a structured explanation describing the major factors influencing the result.

Each explanation compares both teams across:

- Recent Form
- Win Percentage
- Goal Difference
- Overall Strength Difference

Future versions may include:

- Tournament Importance
- Head-to-Head adjustment
- Machine Learning confidence

---

## Rationale

Explainable predictions improve:

- Transparency
- Debugging
- User trust
- Educational value

They also distinguish the platform from black-box prediction models.

---

## Consequences

### Positive

- Easy to understand predictions.
- Simplifies debugging.
- Suitable for dashboard visualisation.

### Negative

- Explanations must remain synchronised with prediction logic.

