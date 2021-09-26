from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    ticker = Column(String, nullable=False)
    company = Column(String)
    sector = Column(String)
    industry = Column(String)
    country = Column(String)
    market__cap = Column(String)
    p_e = Column(Float)
    fwd__p_e = Column(Float)
    peg = Column(Float)
    p_s = Column(Float)
    p_b = Column(Float)
    dividend = Column(Float)
    roa = Column(Float)
    roe = Column(Float)
    roi = Column(Float)
    curr__r = Column(Float)
    quick__r = Column(Float)
    debt_eq = Column(Float)
    gross__m = Column(Float)
    oper__m = Column(Float)
    profit__m = Column(Float)
    avg__volume = Column(String)
    recom = Column(Float)

    def __repr__(self) -> str:
        return f'<Stock {self.ticker}>'

    @property
    def serialize(self) -> dict:
        """Return item in serializeable format."""

        return {
            'Ticker': self.ticker,
            'Company': self.company,
            'Sector': self.sector,
            'Industry': self.industry,
            'Country': self.country,
            'Market Cap': self.market__cap,
            'P/E': self.p_e,
            'Fwd P/E': self.fwd__p_e,
            'PEG': self.peg,
            'P/S': self.p_s,
            'P/B': self.p_b,
            'Dividend': self.dividend,
            'ROA': self.roa,
            'ROE': self.roe,
            'ROI': self.roi,
            'Curr R': self.curr__r,
            'Quick R': self.quick__r,
            'Debt/Eq': self.debt_eq,
            'Gross M': self.gross__m,
            'Oper M': self.oper__m,
            'Profit M': self.profit__m,
            'Avg Volume': self.avg__volume,
            'Recom': self.recom,
        }
