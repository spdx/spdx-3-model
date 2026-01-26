# Contributing to the SPDX 3.0 Model

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

There are multiple profiles being developed in parallel for the SPDX 3.0 model.

- During its initial phase of development, a profile working group will
  contribute changes to its own branch in this repository.
  - For example, any changes to the "Future Profile" should be submitted as a
    change request to the `future-profile` branch.
- There will be at least one maintainer per profile in charge of merging any
  profile development changes to the profile-specific branch.
- Once the first "complete" version of a profile is ready,
  the profile maintainer will alert the general SPDX tech group that the
  profile model is ready for review.
- Once alerted, the SPDX tech group will review and provide feedback.
- Once profile proposals have been reviewed and approved, the profile-specific
  branch will be merged to a general `development` branch along with the other
  reviewed profile models.
- Once the profile in `development` branch is stable, its code from the
  `development` branch will be merged to `main`.

At this point the SPDX tech team will re-evaluate the best way to continue
updating individual profiles.

This method of development was agreed upon by the SPDX Tech team on 2023-01-17.

## Translation

Translations of model descriptions are welcome.
Please see [translation.md][translation] for details.

## Profile Maintainers

In accordance with the development model described above,
each profile has at least one maintainer in charge of merging profile-specific
changes to the profile working branch.

To contribute to a specific profile, please open a PR to the profile-specific
branch or reach out to the maintainer of the profile (noted below).

Each profile in active development phase also has their own
[regular meeting time](https://github.com/spdx/meetings#sub-groups-for-specific-topics).

| Profile | Maintainer(s) |
| ----------- | ----------- |
| AI | [Karen Bennet][gh-karen] and [Gopi Krishnan Rajbahadur][gh-gopi] |
| Dataset | [Karen Bennet][gh-karen] and [Gopi Krishnan Rajbahadur][gh-gopi] |
| Build | [Brandon Lum][gh-brandon] and [Nisha Kumar][gh-nisha] |
| Core | [William Bartholomew][gh-william], [Gary O'Neall][gh-gary], and [Kate Stewart][gh-kate] |
| Licensing | [Steve Winslow][gh-steve] and [Alexios Zavras][gh-alexios] |
| Security | [Thomas Steenbergen][gh-thomas], [Adolfo García Veytia][gh-adolfo], and [Rose Judge][gh-rose] |
| Software | [Alexios Zavras][gh-alexios] and [Gary O'Neall][gh-gary] |

[format]: ./docs/format.md
[translation]: ./docs/translation.md
[spdx-tech-list]: https://lists.spdx.org/mailman/listinfo/spdx-tech
[meetings]: https://github.com/spdx/meetings/
[issues]: https://github.com/spdx/spdx-3-model/issues/
[pull-requests]: https://github.com/spdx/spdx-3-model/pulls/
[cla]: CLA.md
[gh-karen]: https://github.com/bk
[gh-gopi]: https://github.com/rgopikrishnan91
[gh-brandon]: https://github.com/lumjjb
[gh-nisha]: https://github.com/nishakm
[gh-william]: https://github.com/iamwillbar
[gh-gary]: https://github.com/goneall
[gh-kate]: https://github.com/kestewart
[gh-steve]: https://github.com/swinslow
[gh-alexios]: https://github.com/zvr
[gh-thomas]: https://github.com/tsteenbe
[gh-adolfo]: https://github.com/puerco
[gh-rose]: https://github.com/rnjudge
