CC      := gcc
CCFLAGS := #-L /home/amirsorouri00/Desktop/opt/ffmpeg/FFmpeg/ #-I
LDFLAGS := -lavutil -lavformat -lavcodec -lswscale -lz -lavutil -lm

TARGETS:= tutorial02
MAINS  := $(addsuffix .o, $(TARGETS) )
OBJ    := #../commons/commons.o # kbd.o command.o display.o $(MAINS)
DEPS   := #../commons/commons.h # defs.h command.h
LIBS   := 	

BUILDPATH	:= #./build/

.PHONY: all clean

all: $(TARGETS)

clean:
	rm -f $(TARGETS) $(OBJ)

$(OBJ): %.o : %.c $(DEPS)
	$(CC) -o $@ $< $(CCFLAGS) 

$(TARGETS): % : $(filter-out $(MAINS), $(OBJ)) %.o
	$(CC) -o $@ $(LIBS) $^ $(CCFLAGS) $(BUILDPATH) $(LDFLAGS)
	echo Build Done
