from tqdm import tqdm
from functools import partial  # tqdm progressbar 오류 잡아주는 코드
tqdm = partial(tqdm, position = 0, leave = True )
