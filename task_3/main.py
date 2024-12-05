from parse import parse

def main():
  keywords = ['design', 'photo', 'web', 'python']
  likes = parse([kw.lower() for kw in keywords])
  
  for like in likes:
    print(f'{like[0]} | {like[1]} | {like[2]}')

if __name__ == "__main__":
  main()