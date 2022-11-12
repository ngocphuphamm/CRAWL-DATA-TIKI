
from crawlTiki.constant.constant import SEARCH_URL, MAIN_URL, ITEM_NUMBER_MAX,QUERY_KEYWORD_SEARCH
import math


class TikiHelperUtil:

    def handle_url(self, keyWord: str, limitProduct: int) -> list[str]:
        try:
            url: str = f'{MAIN_URL}'

            if keyWord is not None:
                url: str = f'{SEARCH_URL}{QUERY_KEYWORD_SEARCH}{keyWord}'

            listUrl: list[str] = [url]

            numbersPageCrawl: int = math.ceil(limitProduct / ITEM_NUMBER_MAX)

            if numbersPageCrawl > 1:
                for numberPage in range(2, numbersPageCrawl+1):
                    listUrl.append(f'{url}?page={numberPage}')
        except BaseException as e:
            raise (e)

        return listUrl
