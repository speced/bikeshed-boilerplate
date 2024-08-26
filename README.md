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
About a minute after it's merged,
an automated "update the manifest" PR will show up
and needs to be merged as well.

If you're adding files for a new group,
look for an existing group's files that generate specs that look similar to what you want.
If you're a W3C group, start with the contents of the `boilerplates/w3c/` folder.
Then update the `boilerplate/doctypes.kdl` file to document the new group.

## Testing Boilerplates Before Adding Them Here

If you want to verify that your new or updated boilerplates work the way you want before you PR this repo,
just put the boilerplates in question into the same folder as your spec file.
Bikeshed looks for boilerplates in the spec's folder first,
before it starts searching thru its own data files.

(If you're using the API version of Bikeshed, or passing Bikeshed a spec on stdin,
there's no way to test new boilerplates.
Install it locally from `pipx` and put the spec into a file.)

## When Are Boilerplates Available?

After a boilerplate change has been merged,
a PR will be automatically created with the appropriate changes to the manifest file.
(This can be done manually by running `./update-manifest` in this folder).

Once that PR is merged, a few minutes later the change will be picked up by [bikeshed-data](https://github.com/tabatkins/bikeshed-data)
(check the commit log to see it),
at which point a `bikeshed update` will bring the new boilerplates in.
Alternately, manually updating the boilerplates with `bikeshed update --skip-manifest --boilerplate` will pull the new files down immediately,
without waiting for `bikeshed-data` to update.
