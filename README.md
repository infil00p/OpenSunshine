OpenSunshine
====================

Here's some code that I wrote months ago as a proof of concept of how easy it is to make a form that encrypts everything that goes into it.  It also strips metadata,
and it may be useful to some groups.  It also is good for proving a point about why it shouldn't take months to make a "secure platform" and to hunt down "web bugs".

What this software DOES NOT do:

 * This software does NOT do anything fancy.  The Python GPG binding takes a public key and encrypts your data.  It's assumed that you have your private key not
 on this servere
 * This software in NO WAY have anything to do with anonymity. 
 * This software is NOT secure out of the box!  It's up to you to create an encrypted file system for it to write to.  It DOES check to make sure that the filesystem 
 exists, and throws up the maintenance page if it's missing.
 * This software alone will NOT save lives.  It's written as a starting point to prove a point.

What the goal of this software is:
 * To prove that 10 hours of messing around with Flask can create something useful

The goal is to write an application that can make the problem of submitting data securely a pure Systems Administration task, and not 
a software development task.  This should be the simplest way one can upload a file.  The more features, the more things can break.  I highly recommend that smarter 
people fork this software and work on it.  If there's a security flaw in any of the libraries that it uses, please submit bugs and patches to the upstream projects.

.
