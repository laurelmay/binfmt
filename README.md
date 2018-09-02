# binfmt_misc config

The details of `binfmt_misc` are well
[documented](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/binfmt-misc.rst)
and
[discussed](https://blog.jessfraz.com/post/nerd-sniped-by-binfmt_misc/).
Basically, `binfmt_misc` lets you tell the kernel how to execute a particular
binary that isn't ELF and that doesn't start with a shebang (`#!`). This means
you can `./` execute files that you usually wouln't be able to.

The scripts in this directory are what I use to configure `binfmt_misc` on my
own system. To configure your system for a particular file type, just run the
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

## Testing

After running the script, you should be able to verify that the installation
worked by running the corresponding file in the `test/` directory.
