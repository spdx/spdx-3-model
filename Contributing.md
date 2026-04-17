# Contributing to the SPDX 3 model

## General

SPDX is always welcoming new contributors!

The discussions are happening on the
[spdx-tech mailing list][spdx-tech-list]
and during our [regular meetings][meetings].

All the details are in: <https://spdx.dev/participate/tech/>

This repository consists of files written in
[a specific Markdown format][format] describing the model classes,
datatypes, properties, and vocabularies which will be used to automatically
create documentation, ontologies, and validation artifacts.
These are organized by profile.

Use [spec-parser][] to validate your Markdown for errors.
For instructions on integrating it with MkDocs to generate and test your
specification HTML, refer to the [build guide][build].

Please submit [a pull request][pull-requests] or [an issue][issues]
for any suggested changes or issues you find.

Significant changes between versions should be logged to
[CHANGELOG.md](CHANGELOG.md).

## Contribution License Agreement

Contributions to this repository are made pursuant to the
[SPDX Community Specification Contributor License Agreement 1.0][cla].
You do not need to submit a signed copy of the contributor license agreement;
by making a contribution to this repo, you agree to the terms set forth in that
agreement.

## Contributing to a specific profile

There are multiple profiles being developed in parallel for the SPDX 3 model.

- During its initial phase of development, a profile working group will
  contribute changes to its own branch in this repository.
  - For example, any changes to the "Future" profile should be submitted as a
    change request to the `future-profile` branch.
- There will be at least one maintainer per profile in charge of merging any
  profile development changes to the profile-specific branch.
- Once the first "complete" version of a profile is ready,
  the profile maintainer will alert the general SPDX tech group that the
  profile model is ready for review.
- Once alerted, the SPDX tech group will review and provide feedback.
- Once profile proposals have been reviewed and approved, the profile-specific
  branch will be merged to a general `develop` branch along with the other
  reviewed profile models.
- Once the profile in `develop` branch is stable, its code from the
  `develop` branch will be merged to `main`.

At this point the SPDX tech team will re-evaluate the best way to continue
updating individual profiles.

This method of development was agreed upon by the SPDX Tech team on 2023-01-17.

## Translation

Translations of model descriptions are welcome.
Please see [translation.md][translation] for details.

## Profile maintainers

In accordance with the development model described above,
each profile has at least one maintainer in charge of merging profile-specific
changes to the profile working branch.

To contribute to a specific profile, please open a PR to the profile-specific
branch or reach out to the maintainer of the profile (noted below).

Each profile in active development phase also has their own
[regular meeting time](https://github.com/spdx/meetings#sub-groups-for-specific-topics).

| Profile | Maintainer(s) |
| ------- | ------------- |
| AI | [Karen Bennet][gh-karen] and [Gopi Krishnan Rajbahadur][gh-gopi] |
| Build | [Brandon Lum][gh-brandon] and [Nisha Kumar][gh-nisha] |
| Core | [William Bartholomew][gh-william], [Gary O'Neall][gh-gary], and [Kate Stewart][gh-kate] |
| Dataset | [Karen Bennet][gh-karen] and [Gopi Krishnan Rajbahadur][gh-gopi] |
| FunctionalSafety | [Nicole Pappler][gh-nicole] |
| Hardware | [Steven Carbno][gh-stevenc] and Alfred Strauch |
| Licensing | [Steve Winslow][gh-steve] and [Alexios Zavras][gh-alexios] |
| Operations | [Ummo Schwarting][gh-ummo] |
| Security | [Thomas Steenbergen][gh-thomas], [Adolfo García Veytia][gh-adolfo], and [Rose Judge][gh-rose] |
| Service | [Gary O'Neall][gh-gary] |
| Software | [Alexios Zavras][gh-alexios] and [Gary O'Neall][gh-gary] |
| SupplyChain | [Steven Carbno][gh-stevenc] and Alfred Strauch |

[format]: ./docs/format.md
[spec-parser]: https://github.com/spdx/spec-parser/
[build]: https://github.com/spdx/spdx-spec/blob/develop/build.md
[translation]: ./docs/translation.md
[spdx-tech-list]: https://lists.spdx.org/mailman/listinfo/spdx-tech
[meetings]: https://github.com/spdx/meetings/
[issues]: https://github.com/spdx/spdx-3-model/issues/
[pull-requests]: https://github.com/spdx/spdx-3-model/pulls/
[cla]: CLA.md
[gh-adolfo]: https://github.com/puerco
[gh-alexios]: https://github.com/zvr
[gh-brandon]: https://github.com/lumjjb
[gh-gary]: https://github.com/goneall
[gh-gopi]: https://github.com/rgopikrishnan91
[gh-nicole]: https://github.com/nicpappler
[gh-nisha]: https://github.com/nishakm
[gh-karen]: https://github.com/bennetkl
[gh-kate]: https://github.com/kestewart
[gh-rose]: https://github.com/rnjudge
[gh-steve]: https://github.com/swinslow
[gh-stevenc]: https://github.com/stevenc-stb
[gh-thomas]: https://github.com/tsteenbe
[gh-ummo]: https://github.com/umm0
[gh-william]: https://github.com/iamwillbar
