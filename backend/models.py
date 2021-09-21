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
    market_cap = Column(String)
    pe = Column(Float)
    forward_pe = Column(Float)
    peg = Column(Float)
    ps = Column(Float)
    pb = Column(Float)
    div = Column(Float)
    roa = Column(Float)
    roe = Column(Float)
    roi = Column(Float)
    curr_r = Column(Float)
    quick_r = Column(Float)
    debt_eq = Column(Float)
    gross_m = Column(Float)
    oper_m = Column(Float)
    profit_m = Column(Float)
    volume = Column(String)

    def __repr__(self) -> str:
        return f'<Stock {self.ticker}>'

    @property
    def serialize(self) -> dict:
        """Return item in serializeable format."""

        return {
            'ticker': self.ticker,
            'company': self.company,
            'sector': self.sector,
            'industry': self.industry,
            'country': self.country,
            'market_cap': self.market_cap,
            'pe': self.pe,
            'forward_pe': self.forward_pe,
            'peg': self.peg,
            'ps': self.ps,
            'pb': self.pb,
            'div': self.div,
            'roa': self.roa,
            'roe': self.roe,
            'roi': self.roi,
            'curr_r': self.curr_r,
            'quick_r': self.quick_r,
            'debt_eq': self.debt_eq,
            'gross_m': self.gross_m,
            'oper_m': self.oper_m,
            'profit_m': self.profit_m,
            'volume': self.volume,
        }
