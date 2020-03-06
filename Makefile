CC := clang -g -Wall -ansi
PRGS := rand

all: $(PRGS)

rand: rand.c
	$(CC) -o $@ $<

clean:
	@rm -f *~ *.o

distclean: clean
	@rm -f $(PRGS)
