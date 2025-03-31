import requests


class Geocoding:
    def __init__(self):
        self.api_url = "https://msearch.gsi.go.jp/address-search/AddressSearch?q={place}"

    def get_coordinate(self, place: str) -> list[float]:
        """
        ジオコーディング
        国土地理院APIを使用して、住所から緯度経度を取得する関数。
        """
        response = requests.get(self.api_url.format(place=place), params={"q": place}).json()

        if "error" in response:
            return "error data"
        if not response:
            return "not data"
        else:
            # レスポンスと施設名が一致する緯度経度を返す
            for row in response:
                if row["properties"]["title"].startswith(place):
                    coordinates = row["geometry"]["coordinates"]
                    return coordinates
            return None
