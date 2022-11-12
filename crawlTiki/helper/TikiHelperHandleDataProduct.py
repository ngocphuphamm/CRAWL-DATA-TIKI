import json


from .TikiHelperImage import TikiHelperImage


from crawlTiki.dto.ObjectDTO import ProductInfoDTO, ImageDTO, ObjectImageDTO
from crawlTiki.dto.ObjectDTO import OptionTypeDTO, OptionTypeProduct


class TikiHelperHandleDataProduct:
    def __init__(self, productInfo: list[str], optionImage: ImageDTO) -> None:
        self.dataProduct: list[str] = productInfo
        self.tikiHelperImage: TikiHelperImage = TikiHelperImage(optionImage)

    def handle_configurable_options(self, listConfigOptions: list[str]) -> list[OptionTypeDTO]:
        result: list[OptionTypeDTO] = []
        try:
            for currIdx in listConfigOptions:
                optionType = OptionTypeDTO(
                    name=currIdx.get('name', ''),
                    values=currIdx.get('values', ''))
                result.append(optionType)
        except BaseException as e:
            raise (e)

        return result

    def handle_configurable_options_product(self, listConfigOptionsProduct: list[str]) -> list[OptionTypeProduct]:
        result: list[OptionTypeProduct] = []
        try:

            for currIdx in listConfigOptionsProduct:
                thumbnailUrl: str = currIdx.get('thumbnail_url', '')
                images: list[str] = currIdx.get('images', '')
                thumbnailUrl: ObjectImageDTO = self.tikiHelperImage.handleDataImage(
                    thumbnailUrl)
                images: list[ObjectImageDTO] = self.tikiHelperImage.handleDataListImage(
                    images)
                optionTypeProduct = OptionTypeProduct(
                    nameProductOption=currIdx.get('name', ''),
                    option1=currIdx.get('option1', ''),
                    option2=currIdx.get('option2', ''),
                    price=currIdx.get('price', ''),
                    thumbnailUrlProductOption=thumbnailUrl,
                    imagesProductOption=images
                )

                result.append(optionTypeProduct)

            return result
        except BaseException as e:
            raise (e)

    def handle_Product(self) -> ProductInfoDTO:
        dataProduct: list[str] = json.loads(self.dataProduct)
        nameProduct: str = dataProduct.get('name', '')
        thumbnailUrl: str = dataProduct.get('thumbnail_url', '')
        priceProduct: int = dataProduct.get('price', '')
        description: str = dataProduct.get('description', '')
        images: list[str] = dataProduct.get('images', '')
        originalPrice: int = dataProduct.get('original_price', '')
        ratingAverageProduct: int = dataProduct.get('rating_average', '')
        discount: int = dataProduct.get('discount', '')
        optionsType: str = dataProduct.get(
            'configurable_options', '')
        optionsProduct: list[str] = dataProduct.get(
            'configurable_products', '')
        try:
            thumbnailUrl: ObjectImageDTO = self.tikiHelperImage.handleDataImage(thumbnailUrl)
            if images != '':
                images: list[ObjectImageDTO] = self.tikiHelperImage.handleDataListImage(images)

        except BaseException as e:
            raise (e)

        if optionsType != '':
            try:
                optionsType: list[OptionTypeDTO] = self.handle_configurable_options(
                    optionsType)
            except BaseException as e:
                raise (e)
        if optionsProduct != '':
            try:
                optionsProduct: list[OptionTypeProduct] = self.handle_configurable_options_product(
                    optionsProduct)
            except BaseException as e:
                raise (e)

        productInfo: ProductInfoDTO = ProductInfoDTO(
            name=nameProduct,
            price=priceProduct,
            originalPrice=originalPrice,
            discount=discount,
            ratingAverageProduct=ratingAverageProduct,
            description=description,
            thumbnailUrl=thumbnailUrl,
            imagesProduct=images,
            optionsType=optionsType,
            optionsProduct=optionsProduct
        )
        return productInfo
