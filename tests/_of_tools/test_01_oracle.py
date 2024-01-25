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

def test_likeliness_roll():
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
        print(f'Проверка циклов "до пересечения": l=4, r={r}')
        r+=1
    l=5
    while l != 9:
        color_pre_act(l,5)
        print(f'Проверка циклов "до пересечения": l={l}, r=5')
        l+=1
    #Неактивные поля
    for l in range(9):
            for r in range(10):
                if not (l == 4 and r < 6) and not (l > 4 and r == 5):
                    color_no_act(l,r)
                    print(f'Проверка циклов "неактивно": l={l}, i={r}')

    browser.get(query.screenshot_saved(f'{link}01_test_likeliness_roll.png'))

def test_plus_0():
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[0].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].should(be.clickable)
    browser.all('[class="MuiTableBody-root css-1xnox0e"]>tr')[0].all(
        '[class="MuiTableRow-root css-o38khb"]>td')[0].click()
    color_act(0,0)
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}02_test_plus_0.png'))