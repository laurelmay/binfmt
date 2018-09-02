# binfmt_misc config

The details of `binfmt_misc` are well
[documented](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/binfmt-misc.rst)
and
[discussed](https://blog.jessfraz.com/post/nerd-sniped-by-binfmt_misc/).

The scripts in this directory are what I use to configure `binfmt` on my own
system. To configure your system for a particular file type, just run the
correlated script.

The files that you run must have the executable bit set.

For example to run a new `.decaf` file:

```
$ chmod +x ./test.decaf
$ ./test.decaf
```

or to run a new `.jar` file:

```
$ chmod +x cool_app.jar
$ ./cool_app.jar
```

of course, `chmod` need only be set the first time the binary is executed.
