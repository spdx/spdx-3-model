# Contributing to the SPDX 3.0 Model

## General
SPDX is always welcoming new contributors! The discussions are happening on the spdx-tech mailing list
and during our weekly meetings. All the details are in: https://spdx.dev/participate/tech/

## Reviewing the SPDX 3.0 Release Candidates
SPDX recently released the first release candidate for the SPDX 3.0 model.  
We expect more release candidates prior to general availability and would welcome review and feedback.

This repository consists of markdown files describing the model classes, properties, and vocabularies which will be used to automatically create documentation, ontologies, and validation artifacts.
These are organized by profile.

Please submit a pull request or issue for any suggested changes or issues you find.

## Contributing to a specific profile
There are multiple profiles being developed in parallel for the SPDX 3.0 Model. During this initial phase of development, each profile working group will contribute changes to its own branch in this repository. For example, any changes to the Build Profile should be submitted as a change request to the `build-profile` branch. There will be at least one maintainer per profile in charge of merging any profile development changes to the profile-specific branch. Once the first "complete" version of a profile is ready, the profile maintainer will alert the general SPDX tech group that the profile model is ready for review.

Once alerted, the SPDX tech group will review and provide feedback. Once profile proposals have been reviewed and approved, the profile-specific branch will be merged to a general `development` branch along with the other reviewed profile models. Once the `development` branch containing all the profile models is stable and ready for release, the code from the `development` branch will be merged to `main`. At this point the SPDX tech team will re-evaluate the best way to continue updating individual profiles.

This method of development was agreed upon by the SPDX Tech team on 2023-01-17.

## Profile Maintainers
In accordance with the development model described above, each profile has at least maintainer in charge of merging profile-specific changes to the profile working branch. To contribute to a specific profile, please open a PR to the profile-specific branch or reach out to the maintainer of the profile (noted below). Each profile also has their own weekly meeting time which can be found [here](https://github.com/spdx/meetings#sub-groups-for-specific-topics).

| Profile | Maintainer(s) |
| ----------- | ----------- |
| AI | Karen Bennet and [Gopi Krishnan Rajbahadur](https://github.com/rgopikrishnan91) |
| Dataset | Karen Bennet and [Gopi Krishnan Rajbahadur](https://github.com/rgopikrishnan91) |
| Core | [William Bartholomew](https://github.com/iamwillbar), [Gary O'Neall](https://github.com/goneall), and [Kate Stewart](https://github.com/kestewart) |
| Build | [Brandon Lum](https://github.com/lumjjb) and [Nisha Kumar](https://github.com/nishakm) |
| Licensing | [Steve Winslow](https://github.com/swinslow) and [Alexios Zavras](https://github.com/zvr) |
| Security   | [Thomas Steenbergen](https://github.com/tsteenbe), [Adolfo García Veytia](https://github.com/puerco), and [Rose Judge](https://github.com/rnjudge) |
| Software | [Alexios Zavras](https://github.com/zvr) and [Gary O'Neall](https://github.com/goneall) |

