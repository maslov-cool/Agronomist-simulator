import asyncio


async def main(plant, soaking_time, germination_time, survival_time):
    print(f'0 Beginning of sowing the {plant} plant')

    print(f'1 Soaking of the {plant} started')
    await asyncio.sleep(soaking_time / 1000)
    print(f'2 Soaking of the {plant} is finished')

    print(f'3 Shelter of the {plant} is supplied')
    await asyncio.sleep(germination_time / 1000)
    print(f'4 Shelter of the {plant} is removed')

    print(f'5 The {plant} has been transplanted')
    await asyncio.sleep(survival_time / 1000)
    print(f'6 The {plant} has taken root')

    print(f'7 Application of fertilizers for {plant}')
    await asyncio.sleep(3 / 1000)
    print(f'7 Fertilizers for the {plant} have been introduced')

    print(f'8 Treatment of {plant} from pests')
    await asyncio.sleep(5 / 1000)
    print(f'8 The {plant} is treated from pests')

    print(f'9 The seedlings of the {plant} are ready')


async def sowing(*args):
    tasks = [
        asyncio.create_task(main(*i))
        for i in args
    ]
    await asyncio.gather(*tasks)


data = [('carrot', 7, 18, 2), ('cabbage', 2, 6, 10), ('onion', 5, 12, 7)]
asyncio.run(sowing(*data))
