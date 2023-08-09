from settings_data.settings import SiteSettings
from site_API.utils.site_api_handler import SiteApiInterface

site = SiteSettings()

headers = {
	"X-RapidAPI-Key": site.api_key.get_secret_value(),
	"X-RapidAPI-Host": site.host_api
}
url = "https://coinlore-cryptocurrency.p.rapidapi.com/api"

querystring_tickers = {"start": "0", "limit": "15"}
querystring_markets = {"id": "90"}

site_api = SiteApiInterface()

if __name__ == "__main__":
	site_api()
