from selene import browser,have, query, be
import requests
from selene.core.wait import Command
import time

def test_start():
    status = requests.get('https://fari.app/oracle')
    if str(status) == '<Response [200]>':
        print('')
        print('Статус Код: ', status)
        browser.config.timeout = 4
        browser.open('/oracle')
    else:
        print('')
        print('Страница не открыта. Код: ', status)
        browser.config.timeout = 0.1

def scroll(x: int, y: int) -> Command:
    return Command(
        f'scroll page by x {x} y {y}',
        lambda browser: browser.driver.execute_script(
            f'window.scrollBy({x}, {y});'
        )
    )

dark_blue = 'rgba(65, 95, 156, 1)'
white = 'rgba(255, 255, 255, 1)'
blue = 'rgba(103, 127, 175, 1)'

def color_act(a,b):
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[a].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[b].should(have.css_property(
        'color', white))
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[a].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[b].should(have.css_property(
        'background-color', dark_blue))
def color_no_act(a,b):
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[a].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[b].should(have.no.css_property(
        'color',white))
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[a].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[b].should(have.no.css_property(
        'background-color',dark_blue))
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[a].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[b].should(have.no.css_property(
        'background-color',blue))
def color_pre_act(a,b):
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[a].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[b].should(have.css_property(
        'color', white))
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[a].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[b].should(have.css_property(
        'background-color', blue))

link = 'C:/_test_screenshots/Fery_app_tests/test_01_oracle/'

def test_default_active():
    browser.element('[class="MuiSnackbarContent-action css-zykra6"]>div>button').click()
    time.sleep(0.5)
    browser.get(scroll(0,300))
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr').should(have.size(9))
    browser.all('[class="MuiTableRow-root MuiTableRow-footer css-o38khb"]>td').should(have.size(10))
    #Активные поля
    color_act(4,0)
    color_act(4,5)
    #Поля до пересечения
    r=1
    print('')
    while r != 5:
        color_pre_act(4,r)
        r+=1
    l=5
    while l != 9:
        color_pre_act(l,5)
        l+=1
    #Неактивные поля
    for l in range(9):
            for r in range(10):
                if not (l == 4 and r < 6) and not (l > 4 and r == 5):
                    color_no_act(l,r)
    browser.get(query.screenshot_saved(f'{link}01_test_default_active.png'))

def test_titles():
    browser.element('[data-cy="oracle.value"]').should(have.text('ДА, НО...'))
    browser.element('[data-cy="oracle.value"]').should(have.attribute(
        'data-cy-value','YesBut'))
    browser.all('[class*="css-cespi2"]')[0].should(have.text('LIKELINESS'))
    browser.all('[class*="css-cespi2"]')[1].should(have.text('ROLL'))
    browser.element('[data-cy="oracle.likeliness.4"]>p').should(have.text(
        'ALMOST GUARANTEED (+4)'))
    browser.element('[data-cy="oracle.likeliness.3"]>p').should(have.text(
        'VERY LIKELY (+3)'))
    browser.element('[data-cy="oracle.likeliness.2"]>p').should(have.text(
        'LIKELY (+2)'))
    browser.element('[data-cy="oracle.likeliness.1"]>p').should(have.text(
        'POSSIBLE (+1)'))
    browser.element('[data-cy="oracle.likeliness.0"]>p').should(have.text(
        '50/50 (0)'))
    browser.element('[data-cy="oracle.likeliness.-1"]>p').should(have.text(
        'IMPROBABLE (-1)'))
    browser.element('[data-cy="oracle.likeliness.-2"]>p').should(have.text(
        'UNLIKELY (-2)'))
    browser.element('[data-cy="oracle.likeliness.-3"]>p').should(have.text(
        'VERY UNLIKELY (-3)'))
    browser.element('[data-cy="oracle.likeliness.-4"]>p').should(have.text(
        'FAR FETCHED (-4)'))

def p_numbers(a,b,c):
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[a].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[b].should(have.text(f'+{c}'))
def m_numbers(a,b,c):
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[a].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[b].should(have.text(f'-{c}'))
def test_numbers():
    #Проверка записи положительных результатов
    r = 2
    n = 1
    while r != 10:
        p_numbers(0,r,n)
        print(f'r={r}, n=+{n}')
        r+=1
        n+=1
    r = 3
    n = 1
    while r != 10:
        p_numbers(1,r,n)
        print(f'r={r}, n=+{n}')
        r+=1
        n+=1
    r = 4
    n = 1
    while r != 10:
        p_numbers(2,r,n)
        print(f'r={r}, n=+{n}')
        r+=1
        n+=1
    r = 5
    n = 1
    while r != 10:
        p_numbers(3,r,n)
        print(f'r={r}, n=+{n}')
        r+=1
        n+=1
    r = 6
    n = 1
    while r != 10:
        p_numbers(4,r,n)
        print(f'r={r}, n=+{n}')
        r+=1
        n+=1
    r = 7
    n = 1
    while r != 10:
        p_numbers(5,r,n)
        print(f'r={r}, n=+{n}')
        r+=1
        n+=1
    r = 8
    n = 1
    while r != 10:
        p_numbers(6,r,n)
        print(f'r={r}, n=+{n}')
        r+=1
        n+=1
    p_numbers(7,9,1)
    #Проверка записи отрицательных результатов

def test_plus4_liken():
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[0].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].should(be.clickable)
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[0].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].click()
    color_act(0,0)
    color_act(0,5)
    r = 1
    print('')
    while r != 5:
        color_pre_act(0,r)
        print(f'Проверка циклов "до пересечения": l=0, r={r}')
        r+=1
    l = 1
    while l != 9:
        color_pre_act(l,5)
        print(f'Проверка циклов "до пересечения": l={l}, r=5')
        l+=1
    for l in range(9):
        for r in range(10):
            if not (l == 0 and r < 6) and not (l > 0 and r == 5):
                color_no_act(l,r)
                print(f'Проверка циклов "без пересечения": l={l}, r={r}')
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}002_test_test_plus4_liken.png'))
def test_plus3_liken():
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[1].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].should(be.clickable)
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[1].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].click()
    color_act(1,0)
    color_act(1,5)
    r = 1
    print('')
    while r != 5:
        color_pre_act(1,r)
        print(f'Проверка циклов "до пересечения": l=1, r={r}')
        r+=1
    l = 2
    while l != 9:
        color_pre_act(l,5)
        print(f'Проверка циклов "до пересечения": l={l}, r=5')
        l+=1
    for l in range(9):
        for r in range(10):
            if not (l == 1 and r < 6) and not (l > 1 and r == 5):
                color_no_act(l,r)
                print(f'Проверка циклов "без пересечения": l={l}, r={r}')
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}003_test_test_plus3_liken.png'))
def test_plus2_liken():
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[2].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].should(be.clickable)
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[2].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].click()
    color_act(2,0)
    color_act(2,5)
    r = 1
    print('')
    while r != 5:
        color_pre_act(2,r)
        print(f'Проверка циклов "до пересечения": l=2, r={r}')
        r+=1
    l = 3
    while l != 9:
        color_pre_act(l,5)
        print(f'Проверка циклов "до пересечения": l={l}, r=5')
        l+=1
    for l in range(9):
        for r in range(10):
            if not (l == 2 and r < 6) and not (l > 2 and r == 5):
                print(f'Проверка циклов "без пересечения": l={l}, r={r}')
                color_no_act(l,r)
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}004_test_test_plus2_liken.png'))
def test_plus1_liken():
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[3].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].should(be.clickable)
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[3].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].click()
    color_act(3,0)
    color_act(3,5)
    r = 1
    print('')
    while r != 5:
        color_pre_act(3,r)
        print(f'Проверка циклов "до пересечения": l=3, r={r}')
        r+=1
    l = 4
    while l != 9:
        color_pre_act(l,5)
        print(f'Проверка циклов "до пересечения": l={l}, r=5')
        l+=1
    for l in range(9):
        for r in range(10):
            if not (l == 3 and r < 6) and not (l > 3 and r == 5):
                color_no_act(l,r)
                print(f'Проверка циклов "без пересечения": l={l}, r={r}')
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}005_test_test_plus1_liken.png'))
def test_plus0_liken():
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[4].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].should(be.clickable)
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[4].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].click()
    color_act(4,0)
    color_act(4,5)
    r = 1
    print('')
    while r != 5:
        color_pre_act(4,r)
        print(f'Проверка циклов "до пересечения": l=4, r={r}')
        r+=1
    l = 5
    while l != 9:
        color_pre_act(l,5)
        print(f'Проверка циклов "до пересечения": l={l}, r=5')
        l+=1
    for l in range(9):
        for r in range(10):
            if not (l == 4 and r < 6) and not (l > 4 and r == 5):
                color_no_act(l,r)
                print(f'Проверка циклов "без пересечения": l={l}, r={r}')
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}006_test_test_plus0_liken.png'))
def test_minus1_liken():
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[5].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].should(be.clickable)
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[5].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].click()
    color_act(5,0)
    color_act(5,5)
    r = 1
    print('')
    while r != 5:
        color_pre_act(5,r)
        print(f'Проверка циклов "до пересечения": l=5, r={r}')
        r+=1
    l = 6
    while l != 9:
        color_pre_act(l,5)
        print(f'Проверка циклов "до пересечения": l={l}, r=5')
        l+=1
    for l in range(9):
        for r in range(10):
            if not (l == 5 and r < 6) and not (l > 5 and r == 5):
                color_no_act(l,r)
                print(f'Проверка циклов "без пересечения": l={l}, r={r}')
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}007_test_test_minus1_liken.png'))
def test_minus2_liken():
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[6].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].should(be.clickable)
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[6].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].click()
    color_act(6,0)
    color_act(6,5)
    r = 1
    print('')
    while r != 5:
        color_pre_act(6,r)
        print(f'Проверка циклов "до пересечения": l=6, r={r}')
        r+=1
    l = 7
    while l != 9:
        color_pre_act(l,5)
        print(f'Проверка циклов "до пересечения": l={l}, r=5')
        l+=1
    for l in range(9):
        for r in range(10):
            if not (l == 6 and r < 6) and not (l > 6 and r == 5):
                color_no_act(l,r)
                print(f'Проверка циклов "без пересечения": l={l}, r={r}')
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}008_test_test_minus2_liken.png'))
def test_minus3_liken():
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[7].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].should(be.clickable)
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[7].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].click()
    color_act(7,0)
    color_act(7,5)
    r = 1
    print('')
    while r != 5:
        color_pre_act(7,r)
        print(f'Проверка циклов "до пересечения": l=7, r={r}')
        r+=1
    l = 8
    while l != 9:
        color_pre_act(l,5)
        print(f'Проверка циклов "до пересечения": l={l}, r=5')
        l+=1
    for l in range(9):
        for r in range(10):
            if not (l == 7 and r < 6) and not (l > 7 and r == 5):
                color_no_act(l,r)
                print(f'Проверка циклов "без пересечения": l={l}, r={r}')
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}009_test_test_minus3_liken.png'))
def test_minus4_liken():
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[8].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].should(be.clickable)
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[8].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].click()
    color_act(8,0)
    color_act(8,5)
    r = 1
    print('')
    while r != 5:
        color_pre_act(8,r)
        print(f'Проверка циклов "до пересечения": l=8, r={r}')
        r+=1
    for l in range(9):
        for r in range(10):
            if not (l == 8 and r < 6):
                color_no_act(l,r)
                print(f'Проверка циклов "без пересечения": l={l}, r={r}')
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}010_test_test_minus4_liken.png'))
