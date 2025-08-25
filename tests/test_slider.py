# def test_slider_v1(browser):
#     slider = Slider(browser)
#     slider.visit()
#     assert slider.slider.exist()
#     assert slider.inp.exist()
#     while not slider.inp.get_dom_attribute('value') == '50':
#          slider.slider.send_keys(Keys.ARROW_RIGHT)
#     assert slider.ino.get_dom_attribute("value") == "50"