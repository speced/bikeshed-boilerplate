# Bikeshed Boilerplate

This repo holds the boilerplate files (header, footer, other "constant" bits of specs) used by [Bikeshed](https://github.com/tabatkins/bikeshed).

Bikeshed's "default" boilerplates are in `boilerplate-v1/default`.
However, an [`Org`](https://speced.github.io/bikeshed/#metadata-org) can override these for every group in the org (by placing them in an `org-FOO` folder),
and individual [`Group`s](https://speced.github.io/bikeshed/#metadata-group) in an org can further override them just for themselves (by placing them in a group folder inside the org's folder).

Within any of these folders, each boilerplate file can exist in a generic form `somename.include`
or a [`Status`](https://speced.github.io/bikeshed/#metadata-status)-specific form `somename-STATUS.include` that is only used when the document is built with that particular status.

Missing files at one level fall back to the higher level (status'd to generic, group to org to default).

## Altering Boilerplates

If you need to change an existing boilerplate for your group,
just send a PR.
Make sure to let me know whether the PR is *finished* or you're *drafting* it.

## Adding or Removing Boilerplates

If you need to add or remove files from an existing group's folder,
just send a PR.

If you're adding files for a new group,
look for an existing group's files that generate specs that look similar to what you want.
(For example, if you're a W3C group, start with the contents of the `boilerplate-v1/org-w3c/` folder.)
Then update the `boilerplate-v1/doctypes.kdl` file to document the new group.

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
a PR will be automatically created with the appropriate changes to the `manifest-v1.kdl` file.
(This can be done manually by running [`.github/workflows/manifest/manifest.py`](https://github.com/speced/bikeshed-boilerplate/tree/main/.github/workflows/manifest).)

Once that PR is merged, a few minutes later the change will be picked up by [bikeshed-data](https://github.com/tabatkins/bikeshed-data)
(check the commit log to see it),
at which point a `bikeshed update` will bring the new boilerplates in.
Alternately, manually updating the boilerplates with `bikeshed update --skip-manifest --boilerplate` will pull the new files down immediately,
without waiting for `bikeshed-data` to update.
