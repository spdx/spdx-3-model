# Contributing to the SPDX 3.0 Model

## General
SPDX is always welcoming new contributors! The discussions are happening on the spdx-tech mailing list
and during our weekly meetings. All the details are in: https://spdx.dev/participate/tech/

## Contributing to a specific profile
There are multiple profiles being developed in parallel for the SPDX 3.0 Model. During this initial phase of development, each profile working group will contribute changes to its own branch in this repository. For example, any changes to the Build Profile should be submitted as a change request to the `build-profile` branch. There will be at least one maintainer per profile in charge of merging any profile development changes to the profile-specific branch. Once the first "complete" version of a profile is ready, the profile maintainer will alert the general SPDX tech group that the profile model is ready for review.

Once alerted, the SPDX tech group will review and provide feedback. Once profile proposals have been reviewed and approved, the profile-specific branch will be merged to a general `development` branch along with the other reviewed profile models. Once the `development` branch containing all the profile models is stable and ready for release, the code from the `development` branch will be merged to `main`. At this point the SPDX tech team will re-evaluate the best way to continue updating individual profiles.

This method of development was agreed upon by the SPDX Tech team on 2023-01-17.

## Profile Maintainers
In accordance with the development model described above, each profile has at least maintainer in charge of merging profile-specific changes to the profile working branch. To contribute to a specific profile, please open a PR to the profile-specific branch or reach out to the maintainer of the profile (noted below). Each profile also has their own weekly meeting time which can be found [here](https://github.com/spdx/meetings#sub-groups-for-specific-topics).

| Profile | Maintainer |
| ----------- | ----------- |
| AI and Data | TBD |
| Core | TBD |
| Build | TBD |
| Licensing | TBD |
| Security   | TBD |
| Software | TBD |

