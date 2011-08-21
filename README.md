OpenSunshine
====================

Here's some code that I wrote months ago as a proof of concept of how easy it is to make a dropbox.  Here are the 
requirements that a modern dropbox has to meet:

 * Must be minimal - This code only requires Python, Flask, Python-GPG and pyPdf to run.  It's designed to work on a lightweight server like nginx or lighttpd. If we 
 add support for more formats, we may need abiword and some zip libraries as well.  This may complicate things and perhaps people should strip the metadata manually
 * Must not be clever - This takes docs, rips out metadata and saves the data somewhere, preferrably encrypted.  If the store does not exist (i.e. restart of 
 the server), the site will be down. (i.e. User intervention is required for an encrypted volume to be mounted, and if the box is tampered, volume locks shut, but 
 that's something that should be up to the admin of the box).

What this software DOES NOT do:

 * This software does NOT do anything fancy.  The Python GPG binding takes a public key and encrypts your data.  It's assumed that you have your private key elsewhere
 * This software in NO WAY have anything to do with anonymity.  This is to solve the dropbox problem that people have trouble with, not anonymity on the Internet
 * This software is NOT secure out of the box!  That's why it's Open Source!

The goal is to write an application that can make the problem of leaking data a pure Systems Administration task, and not 
a software development task.  This should be the simplest way one can upload a file.  The more features, the more things can break.  If other people
want to work on it, PLEASE FORK THIS SOFTWARE.  None of us are as smart as all of us.

Question: Are you going to run a Whistleblower website?
Answer: No.  I'm Canadian and that activity is illegal under the Security of Information Act, and the Criminal Code of Canada. 

Question: If you're not running a site, why did you write it?
Answer: I got sick of the excuses OpenLeaks and WikiLeaks were using to not accept documents.  Based on conversations with legal professionals, the issue of 
whistleblowing is more legal than it is technical, and there needs to be an independent press for the countries that are unable to offer legal source protection 
for journalists (such as Canada).

Question: What licence is this code under?
Answer: 3-Clause BSD.  I do not endorse any of the activities taken with this code for obvious legal reasons


