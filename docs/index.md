

# nslgo Documentation


Notes concerning my experiments with deep learning and go.

Code and experiments have been inspired by the book

- ["Deep Learning and the Game of Go"](https://www.manning.com/books/deep-learning-and-the-game-of-go)
by 
[Max Pumperla](https://maxpumperla.com/) and 
[Kevin Ferguson](https://github.com/macfergus).


See also the github repository of the book:

- [Code and other material for the book "Deep Learning and the Game of Go"](https://github.com/maxpumperla/deep_learning_and_the_game_of_go)

The [githup page of *nslgo*](https://github.com/newskylabs/nslgo) is here:

- [github.com/newskylabs/nslgo](https://github.com/newskylabs/nslgo)


## Installation

You can install *nslgo* with *pip* directly from its *[github repository](https://github.com/newskylabs/nslgo)*:

```sh
pip install git+https://github.com/newskylabs/nslgo
```


## Uninstalling

You can uninstall *nslgo* as follows:

```sh
pip uninstall nslgo
```


## Usage


### Commands

* `nslgo -h` - Help message.
* `nslgo bvb` - Two bots playing randomly against each other.
* `nslgo bvb -h` - Help message for the command `nslgo bvb`


### Two bots playing randomly against each other

```sh
nslgo bvb
```

Or with different board sizes and sleep times:

```sh
nslgo bvb --board-size 5 --sleep 0
nslgo bvb --board-size 7 --sleep 0
nslgo bvb --board-size 9 --sleep 0
nslgo bvb --board-size 19 --sleep 0
```

### A human playing against a random bot

```sh
nslgo hvb
```

Or with different board sizes and sleep times:

```sh
nslgo hvb --board-size 5
nslgo hvb --board-size 7
nslgo hvb --board-size 9
nslgo hvb --board-size 19
```

### For more information use:

```sh
nslgo -h
```

and / or

```sh
nslgo bvb -h
nslgo hvb -h
```


## Comments etc.

If you have any comments, [please drop me a message](http://dietrich.newskylabs.net/email)!

