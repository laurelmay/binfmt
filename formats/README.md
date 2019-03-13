## formats

Each format is specified as a yaml file. The following are the fields used
in the configurations. All fields are required except `dependencies`.

 * **wrapper_name**: Used as the filename for the wrapper script (string)
 * **type**: Either `E` or `M`. E for file extension-based; `M` for magic
   number-based
 * **extension**: The file extension the configuration is for (string)
 * **name**: The name of the format (string)
 * **interpreter**: The entire command that must be used to call the interpreter
(string)
 * **dependencies**:
   * **software**: Requires that a particular command be on the `PATH` (string)
   * **file**: Requires that a particular file exist on disk (string)
