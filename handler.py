from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

class Handler(object):

    def __init__(self):

        self.driver = webdriver.Firefox(executable_path = '/Users/carlos.castedo/PProyectos/cinesa/geckodriver')
        self.driver.get("https://www.cinesa.es/")
        self.driver.maximize_window()

    def navigate(self, cine, pelicula, hora):
        menu_cine = self.driver.find_element_by_xpath("//a[@class=cines and text()='Cines']")
        menu_cine.click()
        time.sleep(1)

        cine = self.driver.find_element_by_xpath("(//a[text()='"+ cine +"'])[2]")
        cine.click()
        time.sleep(5)

        xpath = "//ul[@id='fichaPeli' and not(@class='hidden') and .//a[text()='"+pelicula+"']]//a[@class='horario' and text()='"+hora+"']"
        hora = self.driver.find_element_by_xpath(xpath)
        hora.click()
        time.sleep(5)



    def seleccion_sitios(self, sitios):

        for i in range(len(sitios)):
            add_persona = self.driver.find_element_by_xpath("//div[@class='field f_butaca' and .//span[text()='NORMAL']]//div[@class='btn_mas']")
            add_persona.click()
            time.sleep(1)

        elegir_butacas = self.driver.find_element_by_id("btnResumenPago")
        elegir_butacas.click()
        time.sleep(10)
     

        pos = 50
        fila = 0
        for val in sitios:
            if val['pos'] < pos:
                pos = val['pos']

            fila = val['fila']

        while True:
            xpath_sitio = "//td[contains(@class,'disponible') and @data-butaca='"+str(pos)+"' and @data-fila='"+str(fila)+"']"
            pos_sitio = self.driver.find_element_by_xpath(xpath_sitio)

            hover = ActionChains(self.driver).move_to_element(pos_sitio)
            hover.perform()

            list_sitios_no_preselect = list()
            for val in sitios:
                xpath_preselect = "//td[contains(@class,'disponible preselect') and @data-butaca='"+str(val['pos'])+"' and @data-fila='"+str(val['fila'])+"']"
                try:
                    sitio_preselect = self.driver.find_element_by_xpath(xpath_preselect)
                except:
                    list_sitios_no_preselect.append(val['pos'])
            
            if len(list_sitios_no_preselect) == len(sitios):
                break

            else:
                for val in sitios:
                    if val['pos'] > pos:
                        pos = val['pos']
            
            
        pos_sitio.click()
        time.sleep(1)

        resumen_pago = self.driver.find_element_by_xpath("//input[@value='Resumen y pago >']")
        resumen_pago.click()
        time.sleep(2)

    def login(self, user, password):
        login_boton = self.driver.find_element_by_id("btnIniciaSesion")
        login_boton.click()

        input_user = self.driver.find_element_by_id("user_login")
        input_user.send_keys(user)

        input_pass = self.driver.find_element_by_id("pass_login")
        input_pass.send_keys(password)

        entrar = self.driver.find_element_by_xpath("//input[@value='ENTRAR']")
        entrar.click()

    def pagar(self):
        aceptar_cond = self.driver.find_element_by_xpath("//div[@class='anim_checkbox_check']")
        aceptar_cond.click()

        pagar_tarj = self.driver.find_element_by_id("btrj")
        pagar_tarj.click()
  
    def exit(self):
        self.driver.quit()