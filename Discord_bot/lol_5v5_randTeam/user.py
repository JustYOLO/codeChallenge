# user.py
# lane: int -> 0~4 = top~sup / 5 = any lane

class user:
    __LANE = ["탑", "정글", "미드", "원딜", "서폿"]
    def __init__(self, name: str, pref_lane: int) -> None:
        '''
        type: (str, int) -> None
        input user name in name, input lane info (in integer) in lane
        '''
        self.__user_name = name
        self.__user_lane = pref_lane

    def getName(self) -> str:
        '''
        type: (None) -> str
        returns __user_name
        '''
        return self.__user_name
    def getLane(self) -> int:
        '''
        type: (None) -> int 
        returns __user_lane
        '''
        return self.__user_lane
    def isPrefLane(self) -> bool:
        '''
        type: (None) -> bool
        if user have preffered lane returns True
        '''
        if(self.__user_lane != 5): return False
        else: return True