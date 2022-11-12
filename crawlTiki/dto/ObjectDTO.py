from dataclasses import  dataclass



@dataclass(frozen = True)
class ObjectImageDTO():
    urlImage : str 
    nameImage : str 
    directImage : str 

@dataclass(frozen = True)
class ImageDTO:
    pathName : str
    typeImage : str
 
@dataclass(frozen = True)
class OptionTypeDTO:
    name : str
    values : list[str]    

@dataclass(frozen = True)
class OptionTypeProduct:
    nameProductOption  : str
    option1 : str
    option2 : str
    price : int
    thumbnailUrlProductOption : ObjectImageDTO
    imagesProductOption  : list[ObjectImageDTO]



@dataclass(frozen = True)
class ProductInfoDTO:
    name : str
    price : int
    originalPrice : int
    discount : int
    ratingAverageProduct : int
    thumbnailUrl : ObjectImageDTO
    description : str
    imagesProduct : list[ObjectImageDTO]
    optionsType : list[OptionTypeDTO]
    optionsProduct : list[OptionTypeProduct]



