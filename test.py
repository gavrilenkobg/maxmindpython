import geoip2.database

with geoip2.database.Reader('GeoIP2-Country.mmdb') as reader:

    response = reader.country('94.101.229.41')

    print(response.country.name)