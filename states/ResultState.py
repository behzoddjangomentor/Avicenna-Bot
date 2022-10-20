from aiogram.dispatcher.filters.state import StatesGroup,State
class CheckResult(StatesGroup):
    test_code = State()
    phone = State()
class BlokTestState(StatesGroup):
    global_id = State()
class StudentInfo(StatesGroup):
    one_id = State()