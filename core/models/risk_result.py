from pydantic import BaseModel


class CategoryScore(BaseModel):
    category: str
    score: int
    finding_count: int


class RiskResult(BaseModel):
    overall_score: int
    category_scores: list[CategoryScore]
    total_findings: int
    findings_by_severity: dict[str, int]
