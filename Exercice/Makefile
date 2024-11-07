# Nom du compilateur
CXX = g++

# Options de compilation
CXXFLAGS = -std=c++11 -Wall -Wextra

# Nom de l'exécutable
TARGET = cplusplus

# Fichiers source
SRCS = cplusplus.cpp

# Fichiers objets
OBJS = $(SRCS:.cpp=.o)

# Règle par défaut
all: $(TARGET)

# Règle pour créer l'exécutable
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

# Règle pour créer les fichiers objets
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Règle pour nettoyer les fichiers générés
clean:
	rm -f $(OBJS) $(TARGET)

# Règle pour exécuter le programme
run: $(TARGET)
	./$(TARGET)