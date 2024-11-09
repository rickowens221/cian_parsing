import cianparser

moscow_parser = cianparser.CianParser(location = 'Москва')

data = moscow_parser.get_flats(deal_type='rent_long',rooms = (1,2,"studio"), with_saving_csv=True, additional_settings={"start_page":1, "end_page":5})

print(data)