from  requests import * # type: ignore
from bs4 import * # type: ignore
import sys
import io
import geocoder
from time import sleep

coords = geocoder.ip("me")
city = coords.city
work = Session()
if sys.stdout is not None:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def get_weather():
    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'}
    response = get(f'https://yandex.ru/pogoda/ru/{city}/',headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    pogodadata = soup.find('body').find('div', class_="AppLayoutCommon_overlay__h5IHD").find('div', class_='AppLayoutTypeMain_contentWrapper__mZQ3q').find('div', class_="AppLayoutTypeMain_centerWrapper___mgad").find('div', class_='AppLayoutTypeMain_center__R9r7_').find("main", class_="AppLayoutTypeMain_main__s_v86 AppLayoutTypeMain_main_noOverflow__6aGtv").find("section", class_="AppLayoutTypeMain_content_type_main__3LVsz").find('article').find("div",class_="AppFact_wrap__N4SYB AppFact_wrap_withReportInAlert__O_NZl AppFact_wrap_withAlice__eV9cu")
    znak = pogodadata.find("p",  class_="AppFactTemperature_content__Lx4p9 AppFactTemperature_content_bold__qXi_O AppFact_temperature__v6zX1").find("span", class_="AppFactTemperature_sign__1MeN4 AppFactTemperature_attr__8pcxc").text
    gradus = pogodadata.find("p",  class_="AppFactTemperature_content__Lx4p9 AppFactTemperature_content_bold__qXi_O AppFact_temperature__v6zX1").find("span", class_="AppFactTemperature_value__2qhsG").text
    nebo = pogodadata.find("div", class_="AppFact_warning__8kUUn").find("div" ,class_="AppFact_warning__first__lRqY9").find("span" ,class_="AppFact_warning__first_text___wtkV").text
    veter = pogodadata.find("ul",class_="AppFact_details__OYahy").find("li", class_="AppFact_details__item__QFIXI").text
    vlazhnost = pogodadata.find("ul",class_="AppFact_details__OYahy").find_all("li" ,class_="AppFact_details__item__QFIXI")[2].text
    temp = str(znak)+str(gradus)+"°C"
    data = {'temp':temp, 'vlazhnost':vlazhnost, 'veter': veter, 'nebo': nebo}
    return data

