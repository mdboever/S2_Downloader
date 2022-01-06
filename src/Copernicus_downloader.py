#  Copernicus Downloader - works for All Sentinel data ( Sentinel-1, Sentinel-2 and Sentinel-3)
# Documenation for Sentinelsat API : https://sentinelsat.readthedocs.io/en/stable/api.html#exceptions


from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt


api = SentinelAPI('USERNAME', 'PASSWORD') # use your username and passwrd created for Copernicus Open Access Data Hub

footprint = geojson_to_wkt(read_geojson('PATH/TO/STUDYAREA/study_area.geojson')) # add the path to your study area and it should be in geojson format
products = api.query(footprint,
                     date=('20200101', '20200116'), # date of image sensing
                     platformname='Sentinel-2',
                     cloudcoverpercentage=(0, 30))


# convert to Pandas DataFrame
products_df = api.to_dataframe(products)

# sort and limit to first 5 sorted products
products_df_sorted = products_df.sort_values(['cloudcoverpercentage', 'ingestiondate'], ascending=[True, True])
products_df_sorted = products_df_sorted.head(5)



api.download_all(products_df_sorted.index)
