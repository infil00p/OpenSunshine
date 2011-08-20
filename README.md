OpenSunshine
====================

Here's some code that I wrote months ago as a proof of concept of how easy it is to make a dropbox.  Here are the 
requirements that a modern dropbox has to meet:

 * Must be minimal - This code only requires Python, Flask, and pyPdf to run.  It's designed to work on a lightweight server like nginx or lighttpd. If we 
 add support for more formats, we may need abiword and some zip libraries as well.  Less services running means a smaller attack surface.
 * Must not be clever - This takes docs, rips out metadata and saves the data somewhere, preferrably encrypted.  If the store does not exist (i.e. restart of 
 the server), the site will be down. (i.e. User intervention is required for an encrypted volume to be mounted, and if the box is tampered, volume locks shut, but 
 that's something that should be up to the admin of the box).

The goal is to write an application that can make the problem of leaking data a pure Systems Administration task, and not 
a software development task.  This should be the simplest way one can upload a file.  The more features, the more things can break.  If other people
want to work on it, PLEASE FORK THIS SOFTWARE.

I'm not really a Cypherpunk, but like Cypherpuks, I write code.
