from pydantic import BaseModel


class Stock(BaseModel):
    ticker: str
    company: str = None
    sector: str = None
    industry: str = None
    country: str = None
    market_cap: str = None
    pe: float = None
    forward_pe: float = None
    peg: float = None
    ps: float = None
    pb: float = None
    div: float = None
    roa: float = None
    roe: float = None
    roi: float = None
    curr_r: float = None
    quick_r: float = None
    debt_eq: float = None
    gross_m: float = None
    oper_m: float = None
    profit_m: float = None
    volume: str = None

    class Config:
        orm_mode = True
