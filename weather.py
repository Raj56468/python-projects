import python_weather

import asyncio


async def main() -> None:
  
  
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    

    weather = await client.get('New York')
    
   
    print(weather.temperature)
    
 
    for daily in weather:
      print(daily)
    
      
      for hourly in daily:
        print(f' --> {hourly!r}')

if __name__ == '__main__':
  asyncio.run(main())