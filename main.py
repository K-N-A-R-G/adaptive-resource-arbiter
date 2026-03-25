

# --- SYNC DATA BLOCK: THREADING ---
            self._flag = True
            self._cond.notify_all()

    def clear(self):
        """Reset the internal flag to false.

        Subsequently, threads calling wait() will block until set() is called to

# --- END OF NODE UPDATE ---
