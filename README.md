# Bikeshed Boilerplate

This repo holds the boilerplate files (header, footer, other "constant" bits of specs) used by [Bikeshed](https://github.com/tabatkins/bikeshed).

The top-level files in the `boilerplate/` folder are used by default,
if there's nothing more specific.

The subfolders are for specific groups (the `Group` metadata in a Bikeshed file) to override the defaults with group-specific variants. In there, the filename may also have a status (the `Status` metadata in the Bikeshed file) to further specialize them.

## Altering Boilerplates

If you need to change an existing boilerplate for your group,
just send a PR.

## Adding or Removing Boilerplates

If you need to add or remove files from an existing group's folder,
send a PR.
I will additionally need to regenerate the manifest,
so it might be delayed until I'm at a work computer.

If you're adding files for a new group,
look for an existing group's files that generate specs that look similar to what you want.
If you're a W3C group, start with the contents of the `boilerplates/w3c/` folder.