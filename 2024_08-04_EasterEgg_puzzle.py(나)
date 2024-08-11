# 소개에서 설명된 이스터 에그 퍼즐은 일반적으로 𝑚 × 𝑛 그리드에서 작동하며, 𝑚은 행의 수(2 ≤ 𝑚 ≤ 26)이고 𝑛은 열의 수(2 ≤ 𝑛 ≤ 26)입니다.
# 그리드의 행은 위에서 아래로 대문자 알파벳 순서로 레이블이 지정됩니다. 그리드의 열은 왼쪽에서 오른쪽으로 번호가 매겨지며 1부터 시작합니다.
# 따라서 그리드의 위치는 대문자 알파벳이 행을 나타내고, 숫자가 열을 나타내는 문자열(str)로 표현될 수 있습니다.
# 새로운 퍼즐(EasterEgg)을 만들 때 네 가지 인수를 전달해야 합니다: 𝑖) 그리드의 행 수 𝑚, 𝑖𝑖) 그리드의 열 수 𝑛, 𝑖𝑖𝑖) 이스터 버니의 시작 위치,
# 그리고 𝑖𝑣) 초기 이스터 에그의 위치가 포함된 텍스트 파일의 위치(str). 클래스의 구현은 인수가 유효한 시작 구성을 설명한다고 가정할 수 있으며,
# 이를 명시적으로 확인할 필요는 없습니다: 이스터 버니와 모든 에그는 그리드 경계 내에 위치하며, 이스터 버니의 시작 위치에 에그가 없습니다.
# 퍼즐(EasterEgg)을 내장 함수 str에 전달하면, 각 행이 별도의 줄로 표현되고 빈 칸은 해시 기호(#)로, 에그가 있는 칸은 대문자 O로,
# 이스터 버니가 서 있는 칸은 대문자 X로 표현된 그리드의 문자열 표현을 반환해야 합니다.

# 또한, 퍼즐(EasterEgg)은 최소한 다음 메서드를 지원해야 합니다:
# • 이스터 버니가 현재 서 있는 위치(str)를 반환하는 메서드 bunny.
# • 남아 있는 모든 에그의 위치(str) 세트를 반환하는 메서드 eggs.
# • 이스터 버니가 현재 위치에서 다음으로 이동할 수 있는 모든 위치(str) 세트를 반환하는 메서드 possible_moves.
# • 위치 𝑝(str)를 인수로 받아 이스터 버니가 현재 위치에서 위치 𝑝로 이동할 수 없는 경우, 이스터 버니는 현재 위치를 유지하고
#   메서드는 invalid move라는 메시지와 함께 AssertionError를 발생시켜야 하는 메서드 move. 그렇지 않으면, 이스터 버니는 위치
#   𝑝로 이동하고 해당 위치의 에그를 수집하여 (그리드에서 에그가 사라지도록) 메서드는 호출된 객체에 대한 참조를 반환해야 합니다.
# • 그리드에 더 이상 에그가 없는지 여부를 나타내는 부울 값(bool)을 반환하는 메서드 isempty.
class EasterEgg:
    def __init__(self,r,c,pos,fileName):
        self.row = r
        self.col = c
        self.bunny_position = pos
        self.egg_position = set()
        with open(fileName,'r') as file:
            #print(f"file.readlines : {file.readlines()}")
            for line in file.readlines():
                self.egg_position.add(line.rstrip())
    def bunny(self):
        return self.bunny_position

    def eggs(self):
        return self.egg_position

    def __str__(self):              # 달걀과 토끼의 위치를 담은 board를 표현
        self.s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(1, self.row + 1):
            Egg = ''
            for j in range(1, self.col + 1):
                d = self.s[i - 1] + str(j)
                if d == puzzle.bunny():
                    Egg += 'X'
                elif d in puzzle.eggs():
                    Egg += 'O'
                else:
                    Egg += '#'
            print(Egg)
        return Egg

    def isempty(self):
        return len(self.egg_position) == 0

    def possible_moves(self):
        self.Can = set()
        self.g = 'ABCDEFG'
        self.s = '1234567'
        self.cur = puzzle.bunny()
        if self.cur.index(self.cur[0:1]) - 2 >= 0:
            if self.cur.index(self.cur[1:2]) - 1 >= 0:
                self.Can.add(self.g[self.cur[self.cur.index(self.cur[0:1]) - 2]] + self.s[self.cur.index(self.cur[1:2]) - 1])
            if self.cur.index(self.cur[1:2]) + 1 <= 7:
                self.Can.add(self.g[self.cur[self.cur.index(self.cur[0:1]) - 2]] + self.s[self.cur.index(self.cur[1:2]) + 1])
        if self.cur.index(self.cur[0:1]) + 2 <= 7:
            if self.cur.index(self.cur[1:2]) - 1 >= 0:
                self.Can.add(self.g[self.cur[self.cur.index(self.cur[0:1]) - 2]] + self.s[self.cur.index(self.cur[1:2]) - 1])
            if self.cur.index(self.cur[1:2]) + 1 <= 7:
                self.Can.add(self.g[self.cur[self.cur.index(self.cur[0:1]) - 2]] + self.s[self.cur.index(self.cur[1:2]) + 1])
        if self.cur.index(self.cur[1:2]) - 2 >= 0:
            if self.cur.index(self.cur[0:1]) + 1 <= 7:
                self.Can.add(self.g[self.cur[self.cur.index(self.cur[1:2]) - 2]] + self.s[self.cur.index(self.cur[0:1]) + 1])
            if self.cur.index(self.cur[0:1]) - 1 >= 0:
                self.Can.add(self.g[self.cur[self.cur.index(self.cur[1:2]) - 2]] + self.s[self.cur.index(self.cur[0:1]) - 1])
        if self.cur.index(self.cur[1:2]) + 2 >= 7:
            if self.cur.index(self.cur[0:1]) - 1 >= 0:
                self.Can.add(self.g[self.cur[self.cur.index(self.cur[1:2]) + 2]] + self.s[self.cur.index(self.cur[0:1]) - 1])
            if self.cur.index(self.cur[0:1]) + 1 <= 7:
                self.Can.add(self.g[self.cur[self.cur.index(self.cur[1:2]) - 2]] + self.s[self.cur.index(self.cur[0:1]) + 1])
        if self.cur.index(self.cur[1:2]) < 7:
            for i in range(self.cur.index(self.cur[1:2]) + 1, 8):
                self.Can.add(self.cur[0:1] + self.s[i - 1])
        return self.Can




    def move(self,_next): # _next에 들어온 좌표로 이동 후 자신을 리턴
        pass

if __name__ == "__main__":
    puzzle = EasterEgg(7, 7, 'D4', 'eggs.txt')
    print(puzzle.bunny())
    # 'D4'
    print(sorted(puzzle.eggs()))  # doctest: +SKIP
    # {'A2', 'A3', 'A4', 'A6', 'A7', 'B1', 'B2', 'C2', 'C4', 'C7', 'D1', 'D2', 'D3',
    # 'D5', 'D6', 'E2', 'E4', 'E7', 'F1', 'F2', 'G2', 'G3', 'G4', 'G6', 'G7'}
    print(puzzle)
    # #OOO#OO
    # OO#####
    # #O#O##O
    # OOOXOO#
    # #O#O##O
    # OO#####
    # #OOO#OO
    print(puzzle.isempty())
    # False
    print(puzzle.possible_moves())  # doctest: +SKIP
    # {'B3', 'B5', 'C2', 'C6', 'D5', 'D6', 'D7', 'E2', 'E6', 'F3', 'F5'}
    print(puzzle.move('E2'))
    # #OOO#OO
    # OO#####
    # #O#O##O
    # OOO#OO#
    # #X#O##O
    # OO#####
    # #OOO#OO
    print(puzzle.bunny())
    # 'E2'
    print(puzzle.eggs())  # doctest: +SKIP
    # {'A2', 'A3', 'A4', 'A6', 'A7', 'B1', 'B2', 'C2', 'C4', 'C7', 'D1', 'D2', 'D3',
    # 'D5', 'D6', 'E4', 'E7', 'F1', 'F2', 'G2', 'G3', 'G4', 'G6', 'G7'}
    #
    print(puzzle.isempty())
    # False
    print(sorted(puzzle.possible_moves())) # doctest: +SKIP
    # {'C1', 'C3', 'D4', 'E3', 'E4', 'E5', 'E6', 'E7', 'F4', 'G1', 'G3'}
    print(puzzle.move('B3'))
    # Traceback (most recent call last):
    # AssertionError: invalid move
    print(puzzle.move('B2'))
    # Traceback (most recent call last):
    # AssertionError: invalid move
    print(puzzle.move('G3').move('F1').move('E3').move('G2').move('G4'))
    # #OOO#OO
    # OO#####
    # #O#O##O
    # OOO#OO#
    # ###O##O
    # #O#####
    # ###X#OO
    print(sorted(puzzle.possible_moves())) # doctest: +SKIP
    # {'E3', 'E5', 'F2', 'F6', 'G5', 'G6', 'G7'}
    print(puzzle.move('F2').move('E4').move('D2').move('B1').move('A3'),'\n')
    # # #OXO#OO
    # # #O#####
    # # #O#O##O
    # # O#O#OO#
    # # ######O
    # # #######
    # # #####OO
    print(puzzle.move('C2').move('C4').move('B2').move('D1').move('D3'),'\n')
    # # #O#O#OO
    # # #######
    # # ######O
    # # ##X#OO#
    # # ######O
    # # #######
    # # #####OO
    print(puzzle.move('B4').move('A2').move('A4').move('A6').move('A7'),'\n')
    # ######X
    # #######
    # ######O
    # ####OO#
    # ######O
    # #######
    # #####OO
    print(puzzle.move('C6').move('C7').move('D5').move('E7').move('G6'),'\n')
    # #######
    # #######
    # #######
    # #####O#
    # #######
    # #######
    # #####XO
    print(puzzle.move('G7').move('F5').move('D6').move('D7'),'\n')
    # #######
    # #######
    # #######
    # ######X
    # #######
    # #######
    # #######
    print(puzzle.isempty())
    # True


