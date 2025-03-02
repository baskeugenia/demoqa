from pages.base_page import BasePage
from components.components import WebElement


class WebtablesPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, '#delete-record-1')
        self.btn_add = WebElement(driver, '#addNewRecordButton')

        self.modal_form = WebElement(driver, 'body > div.fade.modal.show')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')

        self.btn_prev = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')
        self.btn_next = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.page_info = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > div > input[type=number]')

        self.btn_edit_4 = WebElement(driver, '#edit-record-4')
        self.btn_delete_4 = WebElement(driver, '#delete-record-4')
        self.cell_first_name_4 = WebElement(driver,
                                            '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)'
                                            )
        
        self.btn_select_size = WebElement(driver,
                                          '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[2]/select',
                                          'xpath'
                                          )

        self.email = WebElement(driver,
                                '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[4]/div[1]',
                                'xpath'
                                )
        self.sort_asc_by_email = WebElement(driver,
                                        '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div.rt-th.rt-resizable-header.-sort-asc.-cursor-pointer',
                                        )
        self.sort_desc_by_email = WebElement(driver,
                                        '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div.rt-th.rt-resizable-header.-sort-desc.-cursor-pointer',
                                        )
