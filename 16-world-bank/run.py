import wbdata as wb

sources = wb.get_source()
print(sources)
indicators = wb.get_indicator(source=2)
print(indicators)

# The below indicator is from a different source
us = wb.get_data('EF.EFM.RANK.XD',country='USA')
print(us)
matching_countries = wb.search_countries('states')
print(matching_countries)
for n in us:
    print(n['date'],':',n['value'])