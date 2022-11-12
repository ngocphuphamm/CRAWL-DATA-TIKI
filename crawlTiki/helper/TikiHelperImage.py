import json
import shortuuid
from urllib.request import urlopen, HTTPError
import pathlib

from crawlTiki.dto.ObjectDTO import ObjectImageDTO, ImageDTO


class TikiHelperImage:
    def __init__(self, images: ImageDTO) -> None:
        self.pathName: str = images.pathName
        self.typeImage: str = images.typeImage
        self.handle_create_folder()

    def handleDataListImage(self, listImages: list[str]) -> list[ObjectImageDTO]:
        result: list[ObjectImageDTO] = []

        try:
            for currIdx in listImages:
                urlImage: ObjectImageDTO = self.handleDataImage(
                    currIdx.get('medium_url', None))
                result.append(urlImage)
        except BaseException as e:
            raise (e)

        return result

    def handleDataImage(self, url: str) -> ObjectImageDTO:
        try:
            cryptoImage: str = shortuuid.uuid()
            nameImage: str = f'{cryptoImage}.{self.typeImage}'
            directImage: str = f'{self.pathName}/{nameImage}'
            flag: bool = self.download_image(url, directImage)

            if flag is True:
                objectImageDTO = ObjectImageDTO(
                    urlImage=url, nameImage=nameImage, directImage=directImage)
                return objectImageDTO

            raise BaseException("Data image handle error")
        except BaseException as e:
            raise (e)

    def download_image(self, urlImage: str, direct: str) -> bool:
        try:
            img = urlopen(urlImage).read()
            open(direct, 'wb').write(img)
            return True
        except HTTPError:
            pass

    def handle_create_folder(self):
        try:
            if self.pathName is None:
                self.pathName = "images"
                pathlib.Path(self.pathName).mkdir(parents=True, exist_ok=True)
        except BaseException as e:
            raise (e)
