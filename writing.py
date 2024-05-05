from time import sleep;

# A function for writing text to the screen with an animation
def write(title: str, s: str, duration: int, autonext: bool = False):
  for i in range(len(title)+1):
    print(f"\r{title[:i]}", end="");
    sleep(0.028);
  for i in range(len(s)+1):
    print(f"\r{title} {s[:i]}", end="");
    sleep(duration/1000);
  if (autonext):
    sleep(0.2);
    print();
  else:
    input();

