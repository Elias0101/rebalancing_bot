from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()


class PortfolioStates(StatesGroup):
    Continue_After_Start = State()
    Set_Budget = State()
    Check_Budget = State()
    Set_Sectors_Proportion = State()